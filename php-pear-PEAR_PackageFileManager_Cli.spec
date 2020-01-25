%define		status		alpha
%define		pearname	PEAR_PackageFileManager_Cli
Summary:	%{pearname} - a command line interface to PEAR_PackageFileManager
Summary(pl.UTF-8):	%{pearname} - interfejs linii poleceń do PEAR_PackageFileManager
Name:		php-pear-%{pearname}
Version:	0.4.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	21bf5aa87671d71a2b27875abe41a152
URL:		http://pear.php.net/package/PEAR_PackageFileManager_Cli/
BuildRequires:	php-pear-PEAR >= 1:1.4.3
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(xml)
Requires:	php-pear
Requires:	php-pear-PEAR >= 1.4.3
Requires:	php-pear-PEAR_PackageFileManager >= 1.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A command line interface to PEAR_PackageFileManager. Use this tool as
a quick alternative to writing a php script to create or edit your
package xml files.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Interfejs linii poleceń do PEAR_PackageFileManager. Narzędzie to może
być użyte jako alternatywa do tworzenia skryptów PHP zajmujących się
tworzeniem bądź edycją plików package.xml.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/PEAR_PackageFileManager_Cli/README .

# bad os
rm usr/bin/scripts/pfm.bat
rmdir usr/bin/scripts

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
install -p ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log README
%attr(755,root,root) %{_bindir}/pfm
%{php_pear_dir}/.registry/*.reg
