Summary:	Genealogical Research and Analysis Management Programming System
Summary(pl):	System programowania do zarządzania badaniami i analizą genealogiczną
Name:		gramps
Version:	1.0.11
Release:	1
License:	GPL
Group:		Applications/Science
Source0:	http://dl.sourceforge.net/gramps/%{name}-%{version}.tar.gz
# Source0-md5:	f934e3cc4e12cce272e24611b143e728
Patch0:		%{name}-locale_names.patch
Patch1:		%{name}-desktop.patch
URL:		http://gramps.sourceforge.net/
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-gnome-gconf
BuildRequires:	python-gnome-ui >= 1.99
BuildRequires:	python-gnome-vfs
BuildRequires:	python-pygtk-gtk >= 1.99
BuildRequires:	python-pygtk-glade >= 1.99
BuildRequires:	python-ReportLab
BuildRequires:	scrollkeeper >= 0.3.5
Requires:	python >= 2.2
Requires:	python-Imaging 
Requires:	python-gnome >= 1.99
Requires:	python-gnome-canvas >= 1.99
Requires:	python-gnome-gconf >= 1.99
Requires:	python-gnome-ui >= 1.99
Requires:	python-pygtk-gtk >= 1.99
Requires:	python-pygtk-glade >= 1.99
Requires:	python-ReportLab
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var/lib

%description
gramps (Genealogical Research and Analysis Management Programming
System) is a GNOME based genealogy program supporting a Python based
plugin system.

%description -l pl
gramps (Genealogical Research and Analysis Management Programming
System - system programowania do zarządzania badaniami i analizą
genealogiczną) to oparty na GNOME program do genealogii obsługujący
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

rm -rf $RPM_BUILD_ROOT%{_localstatedir}/scrollkeeper

%find_lang gramps

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/bin/scrollkeeper-update
%postun	-p /usr/bin/scrollkeeper-update

%files -f gramps.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README TODO
%attr(755,root,root) %{_bindir}/gramps
%attr(755,root,root) %{_libdir}/gramps
%{_datadir}/gramps
%{_datadir}/omf/gramps
%{_desktopdir}/*
%{_pixmapsdir}/gramps.png
%{_mandir}/man1/*
