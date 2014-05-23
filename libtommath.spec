%define major	0
%define libname %mklibname tommath %{major}
%define devname %mklibname tommath -d

Summary:	Portable number theoretic multiple-precision integer library

Name:		libtommath
Version:	0.42.0
Release:	6
Group:		System/Libraries
License:	Public Domain
Url:		http://libtom.org
Source0:	%{url}/files/ltm-%{version}.tar.bz2
Source1:	%{url}/files/ltm-%{version}.tar.bz2.sig
Source100:	libtommath.rpmlintrc
Patch0:		libtommath-makefile.patch
Patch1:		libtommath-0.42.0-libtool-tag-fix.patch
BuildRequires:	ghostscript
BuildRequires:	ghostscript-dvipdf
BuildRequires:	libtool
BuildRequires:	libtiff-progs
BuildRequires:	tetex-dvips
BuildRequires:	tetex-latex

%description
A free open source portable number theoretic multiple-precision integer
library written entirely in C. (phew!). The library is designed to
provide a simple to work with API that provides fairly efficient
routines that build out of the box without configuration.

%package -n	%{libname}
Summary:	Portable number theoretic multiple-precision integer library

Group:		System/Libraries

%description -n	%{libname}
A free open source portable number theoretic multiple-precision integer
library written entirely in C. (phew!). The library is designed to
provide a simple to work with API that provides fairly efficient
routines that build out of the box without configuration.

%package -n	%{devname}
Summary:	Development files for %{name}

Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	tommath-devel = %{version}-%{release}

%description -n %{devname}
The %{devname} package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%apply_patches
find -name \*.c -o -name \*.h|xargs chmod 644

%build
export CFLAGS="%{optflags} -Ofast -funroll-loops"
%make LIBPATH=%{_libdir} -f makefile.shared 
%make -f makefile poster manual docs

%install
export INSTALL_USER=$(id -un)
export INSTALL_GROUP=$(id -gn)

%makeinstall_std INCPATH=%{_includedir}/tommath LIBPATH=%{_libdir} -f makefile.shared

%files -n %{libname}
%doc LICENSE
%{_libdir}/libtommath.so.%{major}*

%files -n %{devname}
%doc bn.pdf poster.pdf tommath.pdf
%dir %{_includedir}/tommath
%{_includedir}/tommath/*
%{_libdir}/libtommath.so

