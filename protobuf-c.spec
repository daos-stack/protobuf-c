Name:           protobuf-c
Version:        1.3.1
Release:        1%{?dist}
Summary:        C bindings for Google's Protocol Buffers

%if 0%{?suse_version} >= 1315
Group:          Development/Libraries/C and C++
License:        BSD-2-Clause
%else
Group:          System Environment/Libraries
License:        BSD
%endif

URL:            https://github.com/protobuf-c/protobuf-c
Source0:        https://github.com/protobuf-c/protobuf-c/releases/download/v%{version}/%{name}-%{version}.tar.gz

%if 0%{?suse_version} >= 1315
BuildRequires:  pkg-config
%else
BuildRequires:  pkgconfig
%endif
BuildRequires:  gcc-c++
BuildRequires:  protobuf-devel

%description
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. This package provides a code generator and run-time
libraries to use Protocol Buffers from pure C (not C++).

%if 0%{?suse_version} >= 1315
%package -n lib%{name}1
Summary: C bindings for Google's Protocol Buffers
License:        BSD-2-Clause
%description -n lib%{name}1
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. This package provides a code generator and run-time
libraries to use Protocol Buffers from pure C (not C++).
%endif

# el7 protobuf is too old to build the compiler
%if "%{?dist}" != ".el7"
%package compiler
Summary: Protocol Buffers C compiler
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description compiler
This package contains a modified version of the Protocol Buffers
compiler for the C programming language called protoc-c.
%endif

%package devel
Summary:        Protocol Buffers C headers and libraries
%if 0%{?suse_version} >= 1315
Group:          Development/Libraries/C and C++
Requires:       lib%{name}1 = %{version}-%{release}
%else
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-compiler = %{version}-%{release}
%endif

%description devel
This package contains protobuf-c headers and libraries.

%prep
%setup -q

# el7 protobuf v2.5.0 is too old to build the compiler
%if "%{?dist}" != ".el7"
%define build_opts --disable-protoc
%else
%define build_opts %{nil}
%endif

%build
%configure --disable-static %{build_opts}
make

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/libprotobuf-c.la

%if 0%{?suse_version} >= 01315
%post -n lib%{name}1 -p /sbin/ldconfig
%postun -n lib%{name}1 -p /sbin/ldconfig
%else
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%if 0%{?suse_version} >= 1315
%files -n lib%{name}1
%else
%files
%endif
%{_libdir}/libprotobuf-c.so.*
%doc TODO LICENSE ChangeLog

# el7 protobuf is too old to build the compiler
%if "%{?dist}" != ".el7"
%files compiler
%defattr(-,root,root,-)
%{_bindir}/protoc-c
%{_bindir}/protoc-gen-c
%endif

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/google
%{_includedir}/protobuf-c
%{_includedir}/google/protobuf-c
%{_libdir}/libprotobuf-c.so
%{_libdir}/pkgconfig/libprotobuf-c.pc

%changelog
* Wed Oct 02 2019 John E. Malmberg <john.e.malmberg@intel.com> - 1.3.1-1
- new upstream release
- Fix most SUSE rpmlint issues
- protoc needs to be disabled for el7 targets

* Thu Apr 04 2019 Brian J. Murrell <brian.murrell@intel.com> - 1.3.0-1
- new upstream release
- disabled protoc

* Thu Jul 07 2016 Adrian Reber <areber@redhat.com> - 1.0.2-3
- rebuilt for ppc64le

* Mon Aug 17 2015 Adrian Reber <areber@redhat.com> - 1.0.2-2
- remove 'ExcludeArch' hack

* Fri Jul 17 2015 Adrian Reber <areber@redhat.com> - 1.0.2-1
- new upstream release
- split off protoc-c into protobuf-c-compiler to reduce runtime
  dependencies of the main package

* Wed Aug 06 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.0.1-1
- new upstream release

* Mon Aug 04 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.0.0-1
- new upstream release (#1126116)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 David Robinson <zxvdr.au@gmail.com> - 0.15-7
- rebuilt for protobuf-2.5.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 12 2011 David Robinson <zxvdr.au@gmail.com> - 0.15-3
- rebuilt for protobuf-2.4.1

* Sun Apr 24 2011 David Robinson <zxvdr.au@gmail.com> - 0.15-2
- Spec file cleanup

* Wed Apr 20 2011 David Robinson <zxvdr.au@gmail.com> - 0.15-1
- New upstream release
- Spec file cleanup

* Mon Jan 17 2011 Bobby Powers <bobby@laptop.org> - 0.14-1
- New upstream release
- Removed -devel dependency on protobuf-devel
- Small specfile cleanups

* Wed May 19 2010 David Robinson <zxvdr.au@gmail.com> - 0.13-2
- Spec file cleanup

* Wed May 19 2010 David Robinson <zxvdr.au@gmail.com> - 0.13-1
- Initial packaging
