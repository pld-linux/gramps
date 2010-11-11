Summary:	Genealogical Research and Analysis Management Programming System
Summary(pl.UTF-8):	System programowania do zarządzania badaniami i analizą genealogiczną
Name:		gramps
Version:	3.2.4
Release:	1
License:	GPL v2
Group:		Applications/Science
Source0:	http://downloads.sourceforge.net/gramps/%{name}-%{version}.tar.gz
# Source0-md5:	b04a078ca9986ff7a3027676df93c30f
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
BuildRequires:	python-gnome-devel >= 2.6.0
BuildRequires:	python-pygtk-devel >= 2:2.10.0
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

sed -i -e 's|gramps.py|gramps.pyc|' gramps.sh.in
cp %{_datadir}/gnome-doc-utils/gnome-doc-utils.make .

%build
%{__intltoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install \
	--disable-mime-install \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install src/images/gramps.png $RPM_BUILD_ROOT%{_pixmapsdir}
rm -rf $RPM_BUILD_ROOT%{_datadir}/mime-info
rm -rf $RPM_BUILD_ROOT%{_datadir}/application-registry
rm -rf $RPM_BUILD_ROOT%{_datadir}/gramps/COPYING

%find_lang gramps --with-gnome

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
%doc AUTHORS FAQ NEWS README TODO
%attr(755,root,root) %{_bindir}/gramps

%dir %{_datadir}/gramps
%{_datadir}/gramps/*.py*
%{_datadir}/gramps/DateHandler
%{_datadir}/gramps/Filters
%{_datadir}/gramps/GrampsLocale
%{_datadir}/gramps/GrampsLogger
%{_datadir}/gramps/Merge
%{_datadir}/gramps/PluginUtils
%{_datadir}/gramps/ReportBase
%{_datadir}/gramps/Simple
%{_datadir}/gramps/cli
%{_datadir}/gramps/data
%{_datadir}/gramps/docgen
%{_datadir}/gramps/example
%{_datadir}/gramps/gen
%{_datadir}/gramps/glade
%{_datadir}/gramps/gui
%{_datadir}/gramps/images
%{_datadir}/gramps/mapstraction
%{_datadir}/gramps/plugins

%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/mimetypes/*
%{_pixmapsdir}/gramps.png

%{_datadir}/mime/packages/gramps.xml

%{_mandir}/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(sv) %{_mandir}/sv/man1/*
