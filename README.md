# flask-restful

[![Build Status](https://travis-ci.com/RuiCoreSci/flask-restful.svg?branch=master)](https://travis-ci.com/RuiCoreSci/flask-restful) [![Coverage Status](https://coveralls.io/repos/github/RuiCoreSci/flask-restful/badge.svg?branch=master)](https://coveralls.io/github/RuiCoreSci/flask-restful?branch=master) [![codebeat badge](https://codebeat.co/badges/2c118356-0bab-4888-87a1-43acc91e9c72)](https://codebeat.co/projects/github-com-ruicoresci-flask-restful-master) ![python3.8](https://img.shields.io/badge/language-python3.8-blue.svg) ![framework](https://img.shields.io/badge/framework-flask--restful-blue) ![issues](https://img.shields.io/github/issues/RuiCoreSci/flask-restful) ![license](https://img.shields.io/github/license/RuiCoreSci/flask-restful)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FRuiCoreSci%2Fflask-restful.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2FRuiCoreSci%2Fflask-restful?ref=badge_shield)

This is a web backend project based on the flask-restful, mainly designed reference from v2ex.com. 
It implements the interfaces of the website v2ex as much as possible, but does not guarantee no missing.

## Table of Contents
- [Require](#require)
- [Usage](#usage)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Require

* Python3.8
* MySql（5.6 or above）

## Usage

* **First** use command like ```CREATE DATABASE flask DEFAULT CHARSET utf8 ``` or GUI tool to create database in your database.
* **Then** modify ```SQLALCHEMY_DATABASE_URI``` and ```SQLALCHEMY_DATABASE_BASE``` in settings.py to your own setting.
* **Last** create run environment and run:
```sh
python3.8 -m venv --clear venv
source ./venv/bin/active
python server.py
```

## Maintainers

[@RuiCore](https://github.com/ruicore)

## Contributing

PRs are accepted.

Small note: If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

Apache2.0 © 2020 ruicore


[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FRuiCoreSci%2Fflask-restful.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2FRuiCoreSci%2Fflask-restful?ref=badge_large)