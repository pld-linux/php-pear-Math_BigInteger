%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	Math_BigInteger
Summary:	%{_pearname} - Pure-PHP arbitrary precission integer arithmetic library
Name:		php-pear-%{_pearname}
Version:	1.0.2
Release:	1
License:	LGPL License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2805de0fae93acf4084574e8419968ec
URL:		http://pear.php.net/package/Math_BigInteger/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Supports base-2, base-10, base-16, and base-256 numbers. Uses the GMP
or BCMath extensions, if available, and an internal implementation,
otherwise.

In PEAR status of this package is: %{_status}.

%prep
%pear_package_setup

install -d examples
mv .%{php_pear_dir}/Math/BigInteger/demo/* examples

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Math/BigInteger.php

%{_examplesdir}/%{name}-%{version}
