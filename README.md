<!-- markdownlint-disable -->
<p align="center">
    <a href="https://github.com/GreyTeamToolbox/">
        <img src="https://cdn.wolfsoftware.com/assets/images/github/organisations/greyteamtoolbox/black-and-white-circle-256.png" alt="GreyTeamToolbox logo" />
    </a>
    <br />
    <a href="https://github.com/GreyTeamToolbox/baseline-package/actions/workflows/cicd.yml">
        <img src="https://img.shields.io/github/actions/workflow/status/GreyTeamToolbox/baseline-package/cicd.yml?branch=master&label=build%20status&style=for-the-badge" alt="Github Build Status" />
    </a>
    <a href="https://github.com/GreyTeamToolbox/baseline-package/blob/master/LICENSE.md">
        <img src="https://img.shields.io/github/license/GreyTeamToolbox/baseline-package?color=blue&label=License&style=for-the-badge" alt="License">
    </a>
    <a href="https://github.com/GreyTeamToolbox/baseline-package">
        <img src="https://img.shields.io/github/created-at/GreyTeamToolbox/baseline-package?color=blue&label=Created&style=for-the-badge" alt="Created">
    </a>
    <br />
    <a href="https://github.com/GreyTeamToolbox/baseline-package/releases/latest">
        <img src="https://img.shields.io/github/v/release/GreyTeamToolbox/baseline-package?color=blue&label=Latest%20Release&style=for-the-badge" alt="Release">
    </a>
    <a href="https://github.com/GreyTeamToolbox/baseline-package/releases/latest">
        <img src="https://img.shields.io/github/release-date/GreyTeamToolbox/baseline-package?color=blue&label=Released&style=for-the-badge" alt="Released">
    </a>
    <a href="https://github.com/GreyTeamToolbox/baseline-package/releases/latest">
        <img src="https://img.shields.io/github/commits-since/GreyTeamToolbox/baseline-package/latest.svg?color=blue&style=for-the-badge" alt="Commits since release">
    </a>
    <br />
    <a href="https://github.com/GreyTeamToolbox/baseline-package/blob/master/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Code%20of%20Conduct-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/GreyTeamToolbox/baseline-package/blob/master/.github/CONTRIBUTING.md">
        <img src="https://img.shields.io/badge/Contributing-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/GreyTeamToolbox/baseline-package/blob/master/.github/SECURITY.md">
        <img src="https://img.shields.io/badge/Report%20Security%20Concern-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/GreyTeamToolbox/baseline-package/issues">
        <img src="https://img.shields.io/badge/Get%20Support-blue?style=for-the-badge" />
    </a>
</p>

## Overview

This is the baseline package template that we use internally when creating new python tools for the [Blue Team Toolbox](https://github.com/BlueTeamToolbox)
and [Red Team Toolbox](https://github.com/RedTeamToolbox). It has all of the basic functionality and workflows needed to create,
build and publish new package to [PyPI](https://pypi.org/).

Base functionality:

1. Command line processing with examples parameters
2. Wrappers for information, warning, error, success and system messages (and associated colours)
3. A global configuration namespace with example configuration
4. Custom exceptions with examples
5. Clear documentation for each function
6. Minimal dependency on external modules

We decided to make this available along with our other tools to allow people to use a well engineered starting point when creating their own tools.

We also have a [baseline project](https://github.com/GreyTeamToolbox/baseline-project) which can be used to create scripts and tools for local
execution. It comes with all the same base functionality but without the package build and publish.

<br />
<p align="right"><a href="https://wolfsoftware.com/"><img src="https://img.shields.io/badge/Created%20by%20Wolf%20on%20behalf%20of%20Wolf%20Software-blue?style=for-the-badge" /></a></p>
