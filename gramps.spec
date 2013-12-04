Summary:	Genealogical Research and Analysis Management Programming System
Summary(pl.UTF-8):	System programowania do zarządzania badaniami i analizą genealogiczną
Name:		gramps
Version:	4.0.2
Release:	1
License:	GPL v2
Group:		Applications/Science
Source0:	http://downloads.sourceforge.net/gramps/%{name}-%{version}.tar.gz
# Source0-md5:	41d9ae797c2eb2da42474aca3cccb6b3
Patch0:		%{name}-icon_path.patch
URL:		http://gramps-project.org/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.3.5
%pyrequires_eq  python-modules
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	hicolor-icon-theme
Requires:	python-gnome-ui >= 2.12.2-2
Suggests:	graphviz
Suggests:	python-ReportLab
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
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install images/gramps.png $RPM_BUILD_ROOT%{_pixmapsdir}

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/mime-info
%{__rm} -r  $RPM_BUILD_ROOT%{_docdir}/%{name}

%py_postclean

%find_lang gramps

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%scrollkeeper_update_post

%postun
%update_desktop_database_postun
%scrollkeeper_update_postun

%files -f gramps.lang
%defattr(644,root,root,755)
%doc AUTHORS FAQ NEWS README TODO example
%attr(755,root,root) %{_bindir}/gramps

%dir %{_datadir}/gramps
%{_datadir}/gramps/*.xml
%{_datadir}/gramps/css
%{_datadir}/gramps/images

%{py_sitescriptdir}/gramps
%{py_sitescriptdir}/gramps-*.egg-info

%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/mimetypes/*
%{_pixmapsdir}/gramps.png

%{_datadir}/appdata/gramps.appdata.xml

%{_datadir}/mime/packages/gramps.xml

%{_mandir}/man1/*
%lang(cs) %{_mandir}/cs/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(pt_BR) %{_mandir}/pt_BR/man1/*
%lang(sv) %{_mandir}/sv/man1/*
