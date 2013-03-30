#
# Conditional build:
%bcond_without	oyranos	# Oyranos Colour Management System
#
Summary:	X Color Management tools
Summary(pl.UTF-8):	Narzędzia X Color Management (do zarządzania kolorami w X)
Name:		xcm
Version:	0.5.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/oyranos/%{name}-%{version}.tar.bz2
# Source0-md5:	dff4b3bea61df71e6aaa450937ebba48
URL:		http://www.oyranos.org/
BuildRequires:	libXcm-devel
%{?with_oyranos:BuildRequires:	oyranos-devel}
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xcm
%attr(755,root,root) %{_bindir}/xcmddc
%attr(755,root,root) %{_bindir}/xcmedid
%attr(755,root,root) %{_bindir}/xcmevents
/lib/udev/rules.d/90-xcm-i2c.rules
%{_mandir}/man1/xcm.1*
%{_mandir}/man1/xcmddc.1*
%{_mandir}/man1/xcmedid.1*
%{_mandir}/man1/xcmevents.1*
