%define major 1
%define libname %mklibname tommath %{major}
%define devname %mklibname tommath -d

Summary:	Portable number theoretic multiple-precision integer library
Name:		libtommath
Version:	1.2.0
Release:	2
Group:		System/Libraries
License:	Public Domain
Url:		https://github.com/libtom/libtommath
Source0:	https://github.com/libtom/libtommath/archive/v%{version}.tar.gz
Source100:	libtommath.rpmlintrc
BuildRequires:	libtool

%description
A free open source portable number theoretic multiple-precision integer
library written entirely in C. (phew!). The library is designed to
provide a simple to work with API that provides fairly efficient
routines that build out of the box without configuration.

%package -n %{libname}
Summary:	Portable number theoretic multiple-precision integer library
Group:		System/Libraries

%description -n %{libname}
A free open source portable number theoretic multiple-precision integer
library written entirely in C. (phew!). The library is designed to
provide a simple to work with API that provides fairly efficient
routines that build out of the box without configuration.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	tommath-devel = %{EVRD}

%description -n %{devname}
The %{devname} package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%set_build_flags
export CFLAGS="%{optflags} -Ofast -funroll-loops"
%make_build LDFLAGS="%{build_ldflags}" CC=%{__cc} LIBPATH=%{_libdir} -f makefile.shared

%install
export INSTALL_USER=$(id -un)
export INSTALL_GROUP=$(id -gn)

%make_install INCPATH=%{_includedir}/ LIBPATH=%{_libdir} -f makefile.shared

%files -n %{libname}
%{_libdir}/libtommath.so.%{major}*

%files -n %{devname}
%doc LICENSE
%{_includedir}/*.h
%{_libdir}/libtommath.so
%{_libdir}/pkgconfig/libtommath.pc
