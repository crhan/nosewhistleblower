__author__ = 'francisl'

import logging
import os
import json
import socket

from nose.plugins import Plugin


log = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
log.addHandler(ch)


class NoseWhistleblower(Plugin):
    name = 'nose-whistleblower'
    score = 150
    enabled = True

    def __init__(self):
        super(NoseWhistleblower, self).__init__()
        self.tests = 0
        self.success = 0
        self.failures = 0
        self.errors = 0

    def options(self, parser, env=os.environ):
        super(NoseWhistleblower, self).options(parser, env=env)
        parser.add_option("--disable-whistleblower",
                          action="store_true",
                          default=False,
                          dest="disable_whistleblower",
                          help="disable desktop notification")

    def configure(self, options, conf):
        super(NoseWhistleblower, self).configure(options, conf)
        if not options.disable_whistleblower:
            self.enabled = True

        print("config option : %s" % options.disable_whistleblower)


    def begin(self):
        """  Begin recording coverage information. """
        log.debug("Coverage begin")

    def finalize(self, result):
        name = os.getcwd().split("/")[-1].split(".")[0]
        runner = self.__class__.__name__.split(".")[0]

        log.info('Runner: %s' % runner)
        log.info('Name: %s' % name)
        log.info('Success: %s' % result.testsRun)
        log.info('Failures: %s' % len(result.failures))
        log.info('Errors: %s' % len(result.errors))
        log.info('skipped: %s' % len(result.skipped))

        t = '-title {!r}'.format("%s - %s" % (runner, "Success" if result.wasSuccessful() else "Failed"))
        s = '-subtitle {!r}'.format(name)
        m = '-message "Success: %s | Failures: %s | Errors: %s | Skipped: %s"'} % \
                                   (result.testsRun, len(result.failures), len(result.errors), len(result.skipped))
        os.system('terminal-notifier {}'.format(' '.join([t, s, m])))

    def addSuccess(self, test):
        self.tests += 1
        self.success += 1

    def addFailure(self, test, err):
        log.info("an failures")
        self.tests += 1
        self.failures += 1

    def addError(self, test, err):
        log.info("an error")
        self.tests += 1
        self.errors += 1