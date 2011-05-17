%define	major 0
%define libname	%mklibname cmph %{major}
%define develname %mklibname -d cmph

Summary:	C Minimal Perfect Hashing Library
Name:		cmph
Version:	1.1
Release:	%mkrel 1
Group:		System/Libraries
License:	LGPL
URL:		http://cmph.sourceforge.net/
Source0:	http://sourceforge.net/projects/cmph/files/cmph/cmph-%{version}/cmph-%{version}.tar.gz
Patch0:		cmph-1.1-no_examples.diff
Patch1:		cmph-1.1-no_-Werror.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
C Minimal Perfect Hashing Library is a portable LGPL library to create and to
work with minimal perfect hashing functions. The library encapsulates the
newest and more efficient algorithms available in the literature in an
easy-to-use, production-quality, fast API. The library is designed to work with
big entries that cannot fit in the main memory. It has been used successfully
for constructing minimal perfect hashing functions for sets with billions of
keys.

This package contains the cmph command line tool to generate and query minimal
perfect hash functions.

%package -n	%{libname}
Summary:	C Minimal Perfect Hashing Library
Group:          System/Libraries

%description -n	%{libname}
C Minimal Perfect Hashing Library is a portable LGPL library to create and to
work with minimal perfect hashing functions. The library encapsulates the
newest and more efficient algorithms available in the literature in an
easy-to-use, production-quality, fast API. The library is designed to work with
big entries that cannot fit in the main memory. It has been used successfully
for constructing minimal perfect hashing functions for sets with billions of
keys.

%package -n	%{develname}
Summary:	The development files for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}
Requires:	%{libname} >= %{version}

%description -n	%{develname}
C Minimal Perfect Hashing Library is a portable LGPL library to create and to
work with minimal perfect hashing functions. The library encapsulates the
newest and more efficient algorithms available in the literature in an
easy-to-use, production-quality, fast API. The library is designed to work with
big entries that cannot fit in the main memory. It has been used successfully
for constructing minimal perfect hashing functions for sets with billions of
keys.

This package contains the development files for %{name}

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p0

%build
autoreconf -fi

%configure2_5x

%make

%check
make check

%install
rm -rf %{buildroot}

%makeinstall_std

# cleanup
rm -f %{buildroot}%{_libdir}/*.*a

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/cmph
%{_mandir}/man1/cmph.1*

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS README COPYING NEWS README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc ChangeLog
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/cmph.pc

