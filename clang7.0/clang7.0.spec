%define debug_package %{nil}
%define base_name clang
%global ver_major_minor 7.0
Name: %{base_name}%{ver_major_minor}
Version: %{ver_major_minor}.0
%define src_dir %{base_name}-70
Release: 0%{?dist}
Summary: A C language family front-end for LLVM
License: NCSA
Group: Development/Languages
URL: http://llvm.org
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: clang
BuildRequires: /usr/local/llvm-%{ver_major_minor}/bin/llvm-config
BuildRequires: glibc-devel     
BuildRequires: glibc
BuildRequires: zlib-devel ncurses-devel
%undefine _disable_source_fetch
Source0: https://hephaistos.lpp.polytechnique.fr/data/mirrors/clang/%{src_dir}.tar.gz
%define  SHA256SUM0 4fad50935400f4f6595e605709f1d0d443c82a33a64f6e8ee81e356572146029
%description
clang: noun
	
    1. A loud, resonant, metallic sound.
	
    2. The strident call of a crane or goose.
	
    3. C-language family front-end toolkit.
	
 
	
The goal of the Clang project is to create a new C, C++, Objective C
	
and Objective C++ front-end for the LLVM compiler. Its tools are built
	
as libraries and designed to be loosely-coupled and extensible.

%prep
echo "%SHA256SUM0 %SOURCE0" | sha256sum -c -
%setup -qn %{src_dir}

%build
mkdir build && cd build
CC=clang CXX=clang++ cmake -DLLVM_CONFIG:STRING=/usr/local/llvm-%{ver_major_minor}/bin/llvm-config -DBUILD_SHARED_LIBS:BOOL=false -DCMAKE_BUILD_TYPE:STRING=Release -DCMAKE_INSTALL_PREFIX:PATH=%{_usr}/local/%{base_name}-%{ver_major_minor} ..

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} -C build


%files
%{_usr}/local/%{base_name}-%{ver_major_minor}/*

%changelog

* Mon Dec 31 2018 Alexis Jeandet <alexis.jeandet@member.fsf.org> - 7.0.0-0
- First setup

