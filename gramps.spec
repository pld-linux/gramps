Summary:	Genealogical Research and Analysis Management Programming System
Summary(pl.UTF-8):	System programowania do zarządzania badaniami i analizą genealogiczną
Name:		gramps
Version:	5.1.5
Release:	1
License:	GPL v2
Group:		Applications/Science
Source0:	http://downloads.sourceforge.net/gramps/%{name}-%{version}.tar.gz
# Source0-md5:	1185863de6dd30926a50d2083782078d
Patch0:		python-opt2.patch
URL:		http://gramps-project.org/
BuildRequires:	gettext-tools
BuildRequires:	intltool
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.713
Requires:	python3-modules
Requires(post,postun):	desktop-file-utils
Requires:	hicolor-icon-theme
Requires:	python3-gexiv2
Requires:	python3-pycairo
Requires:	python3-pygobject3 >= 3.12
Requires:	python3-pyicu
Requires:	xdg-utils
Recommends:	graphviz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gramps (Genealogical Research and Analysis Management Programming
System) is a GNOME based genealogy program supporting a Python based
plugin system.

%description -l pl.UTF-8
gramps (Genealogical Research and Analysis Management Programming
System - system programowania do zarządzania badaniami i analizą
genealogiczną) to oparty na GNOME program do genealogii obsługujący
system wtyczek w Pythonie.

%prep
%setup -q
%patch0 -p1

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

echo -n "%{_datadir}" > $RPM_BUILD_ROOT%{py3_sitescriptdir}/gramps/gen/utils/resource-path

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/mime-info
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%{__mv} $RPM_BUILD_ROOT%{_localedir}/pt{_PT,}

%find_lang gramps

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f gramps.lang
%defattr(644,root,root,755)
%doc AUTHORS FAQ NEWS README.md TODO example
%attr(755,root,root) %{_bindir}/gramps

%dir %{_datadir}/gramps
%{_datadir}/gramps/*.xml
%{_datadir}/gramps/css
%{_datadir}/gramps/images

%{py3_sitescriptdir}/gramps
%{py3_sitescriptdir}/gramps-*.egg-info

%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/mimetypes/*
%{_datadir}/gramps/grampsxml.dtd
%{_datadir}/gramps/grampsxml.rng
%{_iconsdir}/hicolor/*x*/apps/gramps.png
%{_iconsdir}/hicolor/scalable/apps/gramps.svg
%{_datadir}/metainfo/gramps.appdata.xml
%{_datadir}/mime/packages/gramps.xml

%{_mandir}/man1/*
%lang(cs) %{_mandir}/cs/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(pt_BR) %{_mandir}/pt_BR/man1/*
%lang(sv) %{_mandir}/sv/man1/*
