Summary:	Monitor calibration loader
Name:		xcalib
Version:	0.6
Release:	1
License:	GPL (postcardware)
Group:		X11/Applications
Source0:	http://www.etg.e-technik.uni-erlangen.de/web/doe/xcalib/%{name}-source-%{version}.tar.gz
# Source0-md5:	076f9c28c2d1766d36c424dd1609cdbf
URL:		http://www.etg.e-technik.uni-erlangen.de/web/doe/xcalib/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xcalib is a tiny monitor calibration loader for XFree86 (or X.org) and MS-Windows.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install xcalib $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README* *.icc
%attr(755,root,root) %{_bindir}/*
