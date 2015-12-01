# Internal User Management UI Extension #

[![Build Status](https://travis-ci.org/xebialabs-community/xld-internal-user-plugin.svg?branch=master)](https://travis-ci.org/xebialabs-community/xld-internal-user-plugin)


This helps in management on Internal Users

# Requirements #

* **Deployit requirements**
	* **Deployit**: version 4.5.2+

# Installation #

Build the project:
```
gradlew clean assemble 
```

Copy the extension to the plugins folder of your XLD installation:
```
cp ./build/libs/xld-internal-user-plugin-x.x.x.jar $XLD_HOME/plugins
```
# Snapshot - Internal User Management Tab#

![Visual](/doc-images/usermgttab.png)

# Snapshot - LDAP Validation Tab#

![Visual](/doc-images/ldapvldtab.png)