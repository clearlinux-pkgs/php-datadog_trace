#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v3
# autospec commit: c1050fe
#
Name     : php-datadog_trace
Version  : 0.96.0
Release  : 107
URL      : https://pecl.php.net/get/datadog_trace-0.96.0.tgz
Source0  : https://pecl.php.net/get/datadog_trace-0.96.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
BuildRequires : buildreq-php
BuildRequires : curl-dev
BuildRequires : pcre2-dev
BuildRequires : rustc
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# DD Trace PHP
[![CircleCI](https://circleci.com/gh/DataDog/dd-trace-php/tree/master.svg?style=svg)](https://circleci.com/gh/DataDog/dd-trace-php/tree/master)
[![CodeCov](https://codecov.io/gh/DataDog/dd-trace-php/branch/master/graph/badge.svg?token=eXio8H7vwF)](https://codecov.io/gh/DataDog/dd-trace-php)
[![OpenTracing Badge](https://img.shields.io/badge/OpenTracing-enabled-blue.svg)](http://opentracing.io)
[![OpenTelemetry Badge](https://img.shields.io/badge/OpenTelemetry-enabled-blue.svg)](https://opentelemetry.io)
[![Minimum PHP Version](https://img.shields.io/badge/php-%3E%3D%205.4-8892BF.svg)](https://php.net/)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](LICENSE)
[![Packagist Version](https://img.shields.io/packagist/v/datadog/dd-trace.svg)](https://packagist.org/packages/datadog/dd-trace)
[![Total Downloads](https://img.shields.io/packagist/dt/datadog/dd-trace.svg)](https://packagist.org/packages/datadog/dd-trace)

%prep
%setup -q -n datadog_trace-0.96.0
cd %{_builddir}/datadog_trace-0.96.0
pushd ..
cp -a datadog_trace-0.96.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-datadog_trace
cp %{_builddir}/datadog_trace-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-datadog_trace/ff25afefb5e2f18db479ac6c6b0dc325b322bd4b || :
cp %{_builddir}/datadog_trace-%{version}/LICENSE.Apache %{buildroot}/usr/share/package-licenses/php-datadog_trace/2cd6831faa89469ba68fe484d4d7aa1205d2e776 || :
cp %{_builddir}/datadog_trace-%{version}/LICENSE.BSD3 %{buildroot}/usr/share/package-licenses/php-datadog_trace/5707c40c3ef7eab8b63a20cfc1ca917ba1e9c19a || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
