Summary:	Genealogical Research and Analysis Management Programming System
Summary(pl):	System programowania do zarządzania badaniami i analizą genealogiczną
Name:		gramps
Version:	0.98.0
Release:	0.1
License:	GPL
Group:		Applications/Science
Source0:	http://dl.sourceforge.net/gramps/%{name}-%{version}.tar.gz
# Source0-md5:	027500af2012889b37bfa99ab1e9e382
URL:		http://gramps.sourceforge.net/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	desktop-file-utils >= 0.2.92
BuildRequires:	rpm >= 4.1
BuildRequires:	scrollkeeper >= 0.3.5
Requires:	python >= 2.2
Requires:	python-Imaging 
Requires:	python-gnome >= 1.99
Requires:	python-gnome-canvas >= 1.99
Requires:	python-gnome-gconf >= 1.99
Requires:	python-gnome-ui >= 1.99
Requires:	python-pygtk >= 1.99
Requires:	python-pygtk-glade >= 1.99
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

%build
if [ ! -f configure ]; then
CFLAGS="%{rpmcflags}" ./autogen.sh --prefix=%{_prefix} \
    --localstatedir=%{_localstatedir} --bindir=%{_bindir} \
    --mandir=%{_mandir} --libdir=%{_libdir} --datadir=%{_datadir} \
    --includedir=%{_includedir} --sysconfdir=%{_sysconfdir}
else
	%configure
fi

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall
install -d $RPM_BUILD_ROOT%{_desktopdir}

desktop-file-install --vendor gramps --delete-original \
	--dir $RPM_BUILD_ROOT%{_desktopdir} \
	--add-category Application \
	--add-category Utility \
	$RPM_BUILD_ROOT%{_datadir}/gnome/apps/Applications/gramps.desktop

rm -rf $RPM_BUILD_ROOT%{_localstatedir}/scrollkeeper

%find_lang gramps

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/bin/scrollkeeper-update
%postun	-p /usr/bin/scrollkeeper-update

%files -f gramps.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING-DOCS ChangeLog FAQ NEWS README TODO
%attr(755,root,root) %{_bindir}/gramps
%{_libdir}/gramps
%{_datadir}/gramps
%{_datadir}/omf/gramps
%{_desktopdir}/*
%{_pixmapsdir}/gramps.png
%{_mandir}/man1/*
