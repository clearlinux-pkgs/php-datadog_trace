#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-datadog_trace
Version  : 0.68.1
Release  : 55
URL      : https://pecl.php.net/get/datadog_trace-0.68.1.tgz
Source0  : https://pecl.php.net/get/datadog_trace-0.68.1.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: php-datadog_trace-lib = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : curl-dev
BuildRequires : pcre2-dev

%description
# DD Trace PHP
[![CircleCI](https://circleci.com/gh/DataDog/dd-trace-php/tree/master.svg?style=svg)](https://circleci.com/gh/DataDog/dd-trace-php/tree/master)
[![CodeCov](https://codecov.io/gh/DataDog/dd-trace-php/branch/master/graph/badge.svg?token=eXio8H7vwF)](https://codecov.io/gh/DataDog/dd-trace-php)
[![OpenTracing Badge](https://img.shields.io/badge/OpenTracing-enabled-blue.svg)](http://opentracing.io)
[![Minimum PHP Version](https://img.shields.io/badge/php-%3E%3D%205.4-8892BF.svg)](https://php.net/)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](LICENSE)
[![Packagist Version](https://img.shields.io/packagist/v/datadog/dd-trace.svg)](https://packagist.org/packages/datadog/dd-trace)
[![Total Downloads](https://img.shields.io/packagist/dt/datadog/dd-trace.svg)](https://packagist.org/packages/datadog/dd-trace)

%package lib
Summary: lib components for the php-datadog_trace package.
Group: Libraries

%description lib
lib components for the php-datadog_trace package.


%prep
%setup -q -n datadog_trace-0.68.1
cd %{_builddir}/datadog_trace-0.68.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/ddtrace.so
