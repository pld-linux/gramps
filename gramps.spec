Summary:	Genealogical Research and Analysis Management Programming System
Summary(pl):	System programowania do zarządzania badaniami i analizą genealogiczną
Name:		gramps
Version:	2.0.9
Release:	1
License:	GPL
Group:		Applications/Science
Source0:	http://dl.sourceforge.net/gramps/%{name}-%{version}.tar.gz
# Source0-md5:	900646bf8c2cbf37e3fb81f5892d1141
Patch0:		%{name}-locale_names.patch
Patch1:		%{name}-desktop.patch
URL:		http://gramps.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	GConf2-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	pkgconfig
BuildRequires:	python-gnome-devel >= 2.6.0
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.3.5
%pyrequires_eq  python-modules
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires:	hicolor-icon-theme
Requires:	python-gnome-ui >= 2.12.2-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

sed -i -e 's|gramps.py|gramps.pyc|' gramps.sh.in
rm -rf src/po/no.*

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install \
	--disable-mime-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install src/gramps.png $RPM_BUILD_ROOT%{_pixmapsdir}
rm -rf $RPM_BUILD_ROOT%{_datadir}/mime-info
rm -rf $RPM_BUILD_ROOT%{_datadir}/application-registry
rm -f $RPM_BUILD_ROOT%{_datadir}/gramps/*.py
rm -f $RPM_BUILD_ROOT%{_datadir}/gramps/*/*.py

%find_lang gramps

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gramps.schemas
%update_desktop_database_post
%scrollkeeper_update_post
%banner %{name} -e << EOF
Following packages are strongly recommended to be installed:
- graphviz (for creation of graphs)
- python-ReportLab (for creation of PDF documents)
EOF

%preun
%gconf_schema_uninstall gramps.schemas

%postun
%update_desktop_database_postun
%scrollkeeper_update_postun

%files -f gramps.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README TODO
%attr(755,root,root) %{_bindir}/gramps

%dir %{_datadir}/gramps
%dir %{_datadir}/gramps/gnome
%dir %{_datadir}/gramps/gnome/help
%dir %{_datadir}/gramps/gnome/help/gramps
%{_datadir}/gramps/data
%{_datadir}/gramps/dates
%{_datadir}/gramps/docgen
%{_datadir}/gramps/example
%{_datadir}/gramps/plugins
%{_datadir}/gramps/*.glade
%{_datadir}/gramps/*.jpg
%{_datadir}/gramps/*.png
%{_datadir}/gramps/*.py[co]
%{_datadir}/gramps/gnome/help/gramps/C
%lang(fr) %{_datadir}/gramps/gnome/help/gramps/fr

%{_desktopdir}/*.desktop
%{_iconsdir}/gnome/48x48/mimetypes/*
%{_pixmapsdir}/gramps.png

%{_datadir}/mime/packages/gramps.xml
%{_sysconfdir}/gconf/schemas/gramps.schemas

%{_mandir}/man1/*
%{_omf_dest_dir}/%{name}
