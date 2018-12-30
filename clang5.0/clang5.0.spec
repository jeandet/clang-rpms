%define debug_package %{nil}
%define base_name clang
%global ver_major_minor 5.0
Name: %{base_name}%{ver_major_minor}
Version: %{ver_major_minor}.0
%define src_dir %{base_name}-50
Release: 1%{?dist}
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
%define  SHA256SUM0 9de7efb7398995f8633fa88b17d087d6b4d28ca42b53c71332d39cebbfacbac4
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

* Sat Dec 29 2018 Alexis Jeandet <alexis.jeandet@member.fsf.org> - 5.0.0-1
- Switched to custom llvm

* Fri Dec 28 2018 Alexis Jeandet <alexis.jeandet@member.fsf.org> - 5.0.0-0
- First setup

