#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
#
Summary:	OpenCL C programming language library implementation
Summary(pl.UTF-8):	Implementacja biblioteki języka programowania OpenCL C
Name:		llvm-libclc
Version:	0.2.0
%define	snap	20171128
Release:	0.%{snap}.1
License:	BSD-like or MIT
Group:		Libraries
# git clone http://llvm.org/git/libclc.git
Source0:	libclc-%{snap}.tar.xz
# Source0-md5:	ea25d81625b12e7659881509aa7546cb
Patch0:		build.patch
URL:		http://libclc.llvm.org/
BuildRequires:	clang >= 3.9
BuildRequires:	llvm-devel >= 3.9
BuildRequires:	python >= 1:2.7
BuildRequires:	rpmbuild(macros) >= 1.446
Requires:	llvm-libs >= 3.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libclc is an open source, BSD licensed implementation of the library
requirements of the OpenCL C programming language, as specified by the
OpenCL 1.1 Specification. The following sections of the specification
impose library requirements:

 * 6.1: Supported Data Types
 * 6.2.3: Explicit Conversions
 * 6.2.4.2: Reinterpreting Types Using as_type() and as_typen()
 * 6.9: Preprocessor Directives and Macros
 * 6.11: Built-in Functions
 * 9.3: Double Precision Floating-Point
 * 9.4: 64-bit Atomics
 * 9.5: Writing to 3D image memory objects
 * 9.6: Half Precision Floating-Point

libclc is intended to be used with the Clang compiler's OpenCL
frontend.

%description -l pl.UTF-8
libclc to mająca otwarte źródła, wydana na licencji BSD implementacja
wymagań bibliotecznych języka programowania OpenCL C zgodna ze
specyfikacją OpenCL 1.1. Wymagania biblioteczne wynikają z
następujących sekcji specyfikacji:

 * 6.1: obsługiwane typy danych
 * 6.2.3: jawne konwersje
 * 6.2.4.2: reinterpretacja typów przy użyciu as_type() i as_typen()
 * 6.9: dyrektywy i makra preprocesora
 * 6.11: funkcje wbudowane
 * 9.3: arytmetyka zmiennoprzecinkowa podwójnej precyzji
 * 9.4: 64-bitowe operacje atomowe
 * 9.5: zapis do biektów obrazów 3D w pamięci
 * 9.6: arytmetyka zmiennoprzecinkowa połówkowej precyzji

libclc jest przeznaczona do używania z frontendem OpenCL kompilatora
Clang.

%prep
%setup -q -n libclc
%patch0 -p1

%build
./configure.py \
	--prefix=%{_prefix} \
	--libexecdir=%{_datadir}/clc \
	--pkgconfigdir=%{_npkgconfigdir} \
	--with-llvm-config=/usr/bin/llvm-config

%{__make} \
	VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS.TXT LICENSE.TXT README.TXT www/index.html
%{_includedir}/clc
%{_datadir}/clc
%{_npkgconfigdir}/libclc.pc
