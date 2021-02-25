Summary:	OpenCL C programming language library implementation
Summary(pl.UTF-8):	Implementacja biblioteki języka programowania OpenCL C
Name:		llvm-libclc
Version:	0.2.0
%define	llvm_ver	11.0.1
%define	llvm_dver	%(echo %{llvm_ver} | tr . _)
%define	rel		1
Release:	1.llvm%{llvm_dver}.%{rel}
License:	BSD-like or MIT
Group:		Libraries
#Source0Download: https://github.com/llvm/llvm-project/releases/
Source0:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{llvm_ver}/libclc-%{llvm_ver}.src.tar.xz
# Source0-md5:	a441404cab86a1dd92be69ac8faa1dc7
URL:		https://libclc.llvm.org/
BuildRequires:	clang >= 3.9
BuildRequires:	cmake >= 3.9.2
BuildRequires:	llvm-devel >= 3.9
BuildRequires:	python >= 1:2.7
BuildRequires:	rpmbuild(macros) >= 1.446
Requires:	llvm-libs >= 3.9
BuildArch:	noarch
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
%setup -q -n libclc-%{llvm_ver}.src

%build
install -d build
cd build
# .pc file generation needs CMAKE_INSTALL_{DATADIR,INCLUDEDIR} relative to CMAKE_INSTALL_PREFIX
%cmake .. \
	-DCMAKE_INSTALL_DATADIR=share \
	-DCMAKE_INSTALL_INCLUDEDIR=include

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS.TXT LICENSE.TXT README.TXT www/index.html
%{_includedir}/clc
%{_datadir}/clc
%{_npkgconfigdir}/libclc.pc
