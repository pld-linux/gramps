%define prefix   /usr
%define localstatedir /var/lib
%define _prefix   %prefix
%define _localstatedir %localstatedir

Summary:	Genealogical Research and Analysis Management Programming System.
Name:		gramps
Version:	0.98.0
Release:	0.1
License:	GPL
Group:		Applications/Science
Source0:	http://download.sourceforge.net/gramps/%{name}-%{version}.tar.gz
# Source0-md5:	027500af2012889b37bfa99ab1e9e382
URL:		http://gramps.sourceforge.net/
BuildRequires:	scrollkeeper >= 0.3.5
BuildRequires:	automake >= 1.6
BuildRequires:	autoconf >= 2.52
BuildRequires:	rpm >= 4.1
BuildRequires:	desktop-file-utils >= 0.2.92
Requires:	python >= 2.2
Requires:	python-Imaging 
Requires:	python-gnome >= 1.99
Requires:	python-gnome-canvas >= 1.99
Requires:	python-gnome-gconf >= 1.99
Requires:	python-gnome-ui >= 1.99
Requires:	python-pygtk >= 1.99
Requires:	python-pygtk-glade >= 1.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gramps (Genealogical Research and Analysis Management Programming
System) is a GNOME based genealogy program supporting a Python based
plugin system.

%prep
%setup -q

%build
if [ ! -f configure ]; then
CFLAGS="$MYCFLAGS" ./autogen.sh $MYARCH_FLAGS --prefix=%{_prefix} \
    --localstatedir=%localstatedir --bindir=%{_bindir} \
    --mandir=%{_mandir} --libdir=%{_libdir} --datadir=%{_datadir} \
    --includedir=%{_includedir} --sysconfdir=%{_sysconfdir}
else
  CFLAGS="$MYCFLAGS" %configure
fi

CFLAGS="%{rpmcflags}" make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall
mkdir $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --vendor gramps --delete-original \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications  \
	--add-category Application                     \
	--add-category Utility                         \
	$RPM_BUILD_ROOT%{_datadir}/gnome/apps/Applications/gramps.desktop
%find_lang gramps
rm -rf $RPM_BUILD_ROOT/%{_localstatedir}/scrollkeeper/

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gramps.lang
%defattr(644,root,root,755)

%doc AUTHORS COPYING-DOCS ChangeLog FAQ NEWS README TODO
%doc %{_mandir}/man1/*

%attr(755,root,root) %{_bindir}/gramps

%{_datadir}/applications/*
%{_datadir}/pixmaps/gramps.png

%{_libdir}/gramps
%{_datadir}/gramps
%{_datadir}/omf/gramps

%post
if which scrollkeeper-update>/dev/null 2>&1; then scrollkeeper-update; fi

%postun
if which scrollkeeper-update>/dev/null 2>&1; then scrollkeeper-update; fi
