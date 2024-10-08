#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
# autospec version: v19
# autospec commit: f35655a
#
Name     : gc
Version  : 8.2.8
Release  : 24
URL      : https://github.com/ivmai/bdwgc/releases/download/v8.2.8/gc-8.2.8.tar.gz
Source0  : https://github.com/ivmai/bdwgc/releases/download/v8.2.8/gc-8.2.8.tar.gz
Summary  : A garbage collector for C and C++
Group    : Development/Tools
License  : BSD-2-Clause
Requires: gc-lib = %{version}-%{release}
BuildRequires : file
BuildRequires : libatomic_ops-dev
BuildRequires : pkgconfig(atomic_ops)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Boehm-Demers-Weiser Garbage Collector
This is version 8.2.8 of a conservative garbage
collector for C and C++.

%package dev
Summary: dev components for the gc package.
Group: Development
Requires: gc-lib = %{version}-%{release}
Provides: gc-devel = %{version}-%{release}
Requires: gc = %{version}-%{release}

%description dev
dev components for the gc package.


%package doc
Summary: doc components for the gc package.
Group: Documentation

%description doc
doc components for the gc package.


%package lib
Summary: lib components for the gc package.
Group: Libraries

%description lib
lib components for the gc package.


%prep
%setup -q -n gc-8.2.8
cd %{_builddir}/gc-8.2.8
pushd ..
cp -a gc-8.2.8 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1725987203
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%autogen --disable-static --enable-cplusplus
make  %{?_smp_mflags}

pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%autogen --disable-static --enable-cplusplus
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1725987203
rm -rf %{buildroot}
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/gc.h
/usr/include/gc/cord.h
/usr/include/gc/cord_pos.h
/usr/include/gc/ec.h
/usr/include/gc/gc.h
/usr/include/gc/gc_allocator.h
/usr/include/gc/gc_backptr.h
/usr/include/gc/gc_config_macros.h
/usr/include/gc/gc_cpp.h
/usr/include/gc/gc_disclaim.h
/usr/include/gc/gc_gcj.h
/usr/include/gc/gc_inline.h
/usr/include/gc/gc_mark.h
/usr/include/gc/gc_pthread_redirects.h
/usr/include/gc/gc_tiny_fl.h
/usr/include/gc/gc_typed.h
/usr/include/gc/gc_version.h
/usr/include/gc/javaxfc.h
/usr/include/gc/leak_detector.h
/usr/include/gc_cpp.h
/usr/lib64/libcord.so
/usr/lib64/libgc.so
/usr/lib64/libgccpp.so
/usr/lib64/libgctba.so
/usr/lib64/pkgconfig/bdw-gc.pc
/usr/share/man/man3/gc.3

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/gc/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libcord.so.1.5.1
/V3/usr/lib64/libgc.so.1.5.4
/V3/usr/lib64/libgccpp.so.1.5.0
/V3/usr/lib64/libgctba.so.1.5.0
/usr/lib64/libcord.so.1
/usr/lib64/libcord.so.1.5.1
/usr/lib64/libgc.so.1
/usr/lib64/libgc.so.1.5.4
/usr/lib64/libgccpp.so.1
/usr/lib64/libgccpp.so.1.5.0
/usr/lib64/libgctba.so.1
/usr/lib64/libgctba.so.1.5.0
