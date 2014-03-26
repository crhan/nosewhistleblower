__author__ = 'francisl'

import logging
import os
import sys
import json
import socket
from nose.plugins import Plugin

log = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
log.addHandler(ch)


class Notifier(object):
    PLATFORM = sys.platform

    @staticmethod
    def notify_mac(result, runner, name, msg):
        t = '-title {!r}'.format("%s - %s" % (runner, "Success" if result.wasSuccessful() else "Failed"))
        s = '-subtitle {!r}'.format(name)
        os.system('terminal-notifier {}'.format(' '.join([t, s, msg])))

    @staticmethod
    def notify_linux(result, runner, name, msg):
        from gi.repository import Notify
        Notify.init("%s" % runner)
        notification = Notify.Notification.new (name, msg, runner)
        notification.show ()

    @staticmethod
    def notify(result, runner, name):
        if Notifier.PLATFORM == "darwin":
            handler = Notifier.notify_mac
        else:
            handler = Notifier.notify_linux

        msg = '-message "Success: %s | Failures: %s | Errors: %s | Skipped: %s"' % \
                (result.testsRun, len(result.failures), len(result.errors), len(result.skipped))
        handler(result, runner, name, msg)


class NoseWhistleblower(Plugin):
    name = 'nose-whistleblower'
    score = 150
    enabled = True

    def __init__(self):
        super(NoseWhistleblower, self).__init__()

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

        Notifier.notify(result, runner, name)