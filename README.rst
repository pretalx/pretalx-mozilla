pretalx modifications for Mozilla events
========================================

This is a plugin for `pretalx`_ that contains modifications to run pretalx
with Mozilla events, most importantly changes in wording.

Wording changes include:

- talk ➡  session
- track ➡  space
- speaker ➡  facilitator
- submission ➡  proposal
- reviewer ➡  wrangler
- submitter ➡  facilitator
- type ➡  session format

Development setup
-----------------

1. Make sure that you have a working `pretalx development setup`_.

2. Clone this repository, eg to ``local/pretalx-mozilla``.

3. Activate the virtual environment you use for pretalx development.

4. Execute ``python setup.py develop`` within this directory to register this application with pretalx's plugin registry.

5. Execute ``make`` within this directory to compile translations.

You then have to activate the en-Mozilla locale by putting the following into your pretalx configuration::

   [lang:en-mozilla]
   name=English (mozilla)
   locale_path=path/to/locale


License
-------

Copyright 2019 Tobias Kunze

Released under the terms of the Apache License 2.0


.. _pretalx: https://github.com/pretalx/pretalx
.. _pretalx development setup: https://docs.pretalx.org/en/latest/developer/setup.html
