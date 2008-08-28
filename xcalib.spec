Summary:	Monitor calibration loader
Summary(pl.UTF-8):	Narzędzie do wczytywania kalibracji monitora
Name:		xcalib
Version:	0.8
Release:	2
License:	GPL (postcardware)
Group:		X11/Applications
Source0:	http://www.etg.e-technik.uni-erlangen.de/web/doe/xcalib/%{name}-source-%{version}.tar.gz
# Source0-md5:	1fbcae44ad8d754512fdd1e5f1b3a7e7
URL:		http://www.etg.e-technik.uni-erlangen.de/web/doe/xcalib/
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
%{__make} fglrx_xcalib \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"
mv xcalib fglrx_xcalib

%{__make} clean
%{__make} xcalib \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_iccdir}}

install xcalib fglrx_xcalib $RPM_BUILD_ROOT%{_bindir}
install *.icc $RPM_BUILD_ROOT%{_iccdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README*
%attr(755,root,root) %{_bindir}/xcalib
%attr(755,root,root) %{_bindir}/fglrx_xcalib
%{_iccdir}/*.icc
