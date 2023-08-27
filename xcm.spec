#
# Conditional build:
%bcond_without	oyranos	# Oyranos Colour Management System
#
Summary:	X Color Management tools
Summary(pl.UTF-8):	Narzędzia X Color Management (do zarządzania kolorami w X)
Name:		xcm
Version:	0.5.4
Release:	1
License:	MIT
Group:		X11/Applications
#Source0Download: https://github.com/oyranos-cms/xcm/releases
Source0:	https://github.com/oyranos-cms/xcm/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	cb96d9a704b182a7dce0fe30c9a7b2de
#URL:		http://www.oyranos.org/
URL:		https://github.com/oyranos-cms/xcm
BuildRequires:	libXcm-devel >= 0.5.3
%{?with_oyranos:BuildRequires:	oyranos-devel >= 0.9.6}
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools which based on libXcm, a library for colour management on X:
- xcmddc requests EDID from a monitor over the i2c bus,
- xcmedid is for parsing EDID data blocks,
- xcmevents observes X11 colour management events.

%description -l pl.UTF-8
Narzędzia oparte na libXcm - bibliotece do zarządzania kolarami w X:
- xcmddc pobiera EDID z monitora poprzez szynę i2c,
- xcmedid analizuje bloki danych EDID,
- xcmevents obserwuje zdarzenia X11 związane z zarządzaniem kolorami.

%prep
%setup -q

%build
%configure \
	%{!?with_oyranos:--without-oyranos}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/xcm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md docs/{AUTHORS,COPYING,ChangeLog}
%attr(755,root,root) %{_bindir}/xcm
%attr(755,root,root) %{_bindir}/xcmddc
%attr(755,root,root) %{_bindir}/xcmedid
%attr(755,root,root) %{_bindir}/xcmevents
%attr(755,root,root) %{_bindir}/xcmhextobin
/lib/udev/rules.d/90-xcm-i2c.rules
%{_mandir}/man1/xcm.1*
%{_mandir}/man1/xcmddc.1*
%{_mandir}/man1/xcmedid.1*
%{_mandir}/man1/xcmevents.1*
%{_mandir}/man1/xcmhextobin.1*
