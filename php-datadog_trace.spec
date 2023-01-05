#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-datadog_trace
Version  : 0.81.1
Release  : 79
URL      : https://pecl.php.net/get/datadog_trace-0.81.1.tgz
Source0  : https://pecl.php.net/get/datadog_trace-0.81.1.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: php-datadog_trace-lib = %{version}-%{release}
Requires: php-datadog_trace-license = %{version}-%{release}
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
Requires: php-datadog_trace-license = %{version}-%{release}

%description lib
lib components for the php-datadog_trace package.


%package license
Summary: license components for the php-datadog_trace package.
Group: Default

%description license
license components for the php-datadog_trace package.


%prep
%setup -q -n datadog_trace-0.81.1
cd %{_builddir}/datadog_trace-0.81.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-datadog_trace
cp %{_builddir}/datadog_trace-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-datadog_trace/ff25afefb5e2f18db479ac6c6b0dc325b322bd4b
cp %{_builddir}/datadog_trace-%{version}/LICENSE.Apache %{buildroot}/usr/share/package-licenses/php-datadog_trace/2cd6831faa89469ba68fe484d4d7aa1205d2e776
cp %{_builddir}/datadog_trace-%{version}/LICENSE.BSD3 %{buildroot}/usr/share/package-licenses/php-datadog_trace/5707c40c3ef7eab8b63a20cfc1ca917ba1e9c19a
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20220829/ddtrace.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-datadog_trace/2cd6831faa89469ba68fe484d4d7aa1205d2e776
/usr/share/package-licenses/php-datadog_trace/5707c40c3ef7eab8b63a20cfc1ca917ba1e9c19a
/usr/share/package-licenses/php-datadog_trace/ff25afefb5e2f18db479ac6c6b0dc325b322bd4b
