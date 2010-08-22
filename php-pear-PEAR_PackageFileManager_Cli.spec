%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	PackageFileManager_Cli
%define		_status		alpha
%define		_pearname	PEAR_PackageFileManager_Cli
Summary:	%{_pearname} - a command line interface to PEAR_PackageFileManager
Summary(pl.UTF-8):	%{_pearname} - interfejs linii poleceń do PEAR_PackageFileManager
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	4
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	3a31573f625cdf28f6aee5e08d152be5
URL:		http://pear.php.net/package/PEAR_PackageFileManager_Cli/
BuildRequires:	php-pear-PEAR >= 1:1.4.3
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.574
Requires:	php-pear
Requires:	php-pear-PEAR >= 1.4.3
Requires:	php-pear-PEAR_PackageFileManager >= 1.6.0
Requires:	php-xml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A command line interface to PEAR_PackageFileManager. Use this tool as
a quick alternative to writing a php script to create or edit your
package xml files.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Interfejs linii poleceń do PEAR_PackageFileManager. Narzędzie to może
być użyte jako alternatywa do tworzenia skryptów PHP zajmujących się
tworzeniem bądź edycją plików package.xml.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
cp -a ./%{php_pear_dir}/.registry/ $RPM_BUILD_ROOT%{php_pear_dir}
install ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%attr(755,root,root) %{_bindir}/pfm
%{php_pear_dir}/.registry/*.reg
