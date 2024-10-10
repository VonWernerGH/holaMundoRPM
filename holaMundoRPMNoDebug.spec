Name:             holaMundoRPM
Version:           1.0.0 
Release:          1%{?dist}
Summary:       Programa holaMundoRPM, imprime "Hola Mundo RPM"

License:          GPLv3
URL:                https://github.com/VonWernerGH/
Source0:         %{name}-%{version}.tar.gz
BuildRequires: gcc 
Requires:         glibc


%description
Programa que imprime "Hola Mundo RPM"

%global debug_package %{nil}

%prep
%setup -q

%build
gcc -Wall -Werror -Wl,--as-needed -O3 -g0 -s -march=native -flto -o %{name} %name.c

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}

%files
%{_bindir}/%{name}
%license docs/GPLv3.txt

%changelog
* Tue Oct 08 2024 Víctor Emmanuel Rivero Alonzo <nospamvr-git@yahoo.com> - 1.0.0-1
- Release de holaMundoRPM
