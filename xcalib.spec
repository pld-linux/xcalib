Summary:	Monitor calibration loader
Summary(pl.UTF-8):	Narzędzie do wczytywania kalibracji monitora
Name:		xcalib
Version:	0.10
Release:	1
License:	GPL (postcardware)
Group:		X11/Applications
#Source0Download: https://github.com/OpenICC/xcalib/releases
Source0:	https://github.com/OpenICC/xcalib/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7495d13e88a6e1ead3b20aa8e0d9a042
URL:		https://github.com/OpenICC/xcalib
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_iccdir		%{_datadir}/color/icc

%description
xcalib is a tiny monitor calibration loader for XFree86 (or X.org) and
MS Windows.

%description -l pl.UTF-8
xcalib to małe narzędzie do wczytywania kalibracji monitora dla
XFree86 (lub X.org) oraz MS Windows.

%prep
%setup -q

%build
%ifarch %{ix86}
%{__make} fglrx_xcalib \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}"
%{__mv} xcalib xcalib_fglrx
%endif

%{__make} clean
%{__make} xcalib \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_iccdir}}

%ifarch %{ix86}
install xcalib_fglrx $RPM_BUILD_ROOT%{_bindir}
%endif
install xcalib $RPM_BUILD_ROOT%{_bindir}
cp -p *.icc $RPM_BUILD_ROOT%{_iccdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README*
%attr(755,root,root) %{_bindir}/xcalib*
%{_iccdir}/bluish.icc
%{_iccdir}/gamma_1_0.icc
%{_iccdir}/gamma_2_2.icc
%{_iccdir}/gamma_2_2_bright.icc
%{_iccdir}/gamma_2_2_lowContrast.icc
