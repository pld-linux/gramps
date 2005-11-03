Summary:	Genealogical Research and Analysis Management Programming System
Summary(pl):	System programowania do zarz±dzania badaniami i analiz± genealogiczn±
Name:		gramps
Version:	2.0.8
Release:	1
License:	GPL
Group:		Applications/Science
Source0:	http://dl.sourceforge.net/gramps/%{name}-%{version}.tar.gz
# Source0-md5:	84f2659b292b5e2abc92a8d56148495b
Patch0:		%{name}-locale_names.patch
Patch1:		%{name}-desktop.patch
URL:		http://gramps.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.3
BuildRequires:	python-gnome-gconf
BuildRequires:	python-gnome-ui >= 2.6.0
BuildRequires:	python-gnome-vfs
BuildRequires:	python-pygtk-gtk >= 2.5.0
BuildRequires:	python-pygtk-glade >= 2.5.0
BuildRequires:	python-ReportLab
BuildRequires:	scrollkeeper >= 0.3.5
Requires:	python >= 2.3
Requires:	python-Imaging 
Requires:	python-gnome >= 2.6.0
Requires:	python-gnome-canvas >= 2.6.0
Requires:	python-gnome-gconf >= 2.6.0 
Requires:	python-gnome-ui >= 2.6.0
Requires:	python-pygtk-gtk >= 2.5.0
Requires:	python-pygtk-glade >= 2.5.0
Requires:	python-ReportLab
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var/lib

%description
gramps (Genealogical Research and Analysis Management Programming
System) is a GNOME based genealogy program supporting a Python based
plugin system.

%description -l pl
gramps (Genealogical Research and Analysis Management Programming
System - system programowania do zarz±dzania badaniami i analiz±
genealogiczn±) to oparty na GNOME program do genealogii obs³uguj±cy
system wtyczek w Pythonie.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

rm -rf src/po/no.*

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_pixmapsdir}
cp src/gramps.png $RPM_BUILD_ROOT%{_pixmapsdir}
rm -rf $RPM_BUILD_ROOT%{_localstatedir}/scrollkeeper
rm -rf $RPM_BUILD_ROOT%{_datadir}/mime-info
rm -rf $RPM_BUILD_ROOT%{_datadir}/application-registry

%find_lang gramps

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gramps.schemas
%update_desktop_database_post
##%scrollkeeper-update_post

%preun
%gconf_schema_uninstall gramps.schemas

%postun
%update_desktop_database_postun
##%scrollkeeper-update_postun

%files -f gramps.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README TODO
%attr(755,root,root) %{_bindir}/gramps
%{_sysconfdir}/gconf/schemas/gramps.schemas
%{_datadir}/gramps
%{_datadir}/mime/packages/gramps.xml
%{_datadir}/mime/magic
%{_datadir}/mime/globs
%{_datadir}/mime/XMLnamespaces
%{_datadir}/mime/application/*
%{_datadir}/omf/gramps
%{_desktopdir}/*.desktop
%{_iconsdir}/gnome/48x48/mimetypes/*
%{_pixmapsdir}/gramps.png
%{_mandir}/man1/*
