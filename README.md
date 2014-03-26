## nosewhistleblower

! Proof of concept

### Idea

Notify the completion and status for all your tests running in the background

### Requirements

- python
- nose

#### OS X

terminal-notifier

    brew install terminal-notifier

#### Linux

- [libnotify](https://developer.gnome.org/notification-spec/)
- [PyGObject](https://wiki.gnome.org/action/show/Projects/PyGObject?action=show&redirect=PyGObject)


### Usage

	python setup.py install

#### to disable

    nosetests --disable-whistleblower


### Todo For first release


* ~~send notification to OS X~~
* detect if terminal-notification is not installed
* send notification to Linux
* contentImage