Name:              holaMundoRPM
Version:       	    1.0.0 
Release:           1%{?dist}
Summary:        Programa holaMundoRPM, imprime "Hola Mundo RPM"

License:           GPLv3
URL:           	    https://github.com/VonWernerGH/
Source0:          %{name}-%{version}.tar.gz
BuildRequires: 	gcc 
Requires:         glibc


%description
Programa que imprime "Hola Mundo RPM"

%prep
%setup -q

%build
gcc -O2 -g -fno-omit-frame-pointer -mtune=generic -fstack-protector-strong -D_FORTIFY_SOURCE=2 -pie -fPIE -o %{name} %{name}.c

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}

%files
%{_bindir}/%{name}

%changelog
* Mon Oct 08 2024 Víctor Emmanuel Rivero Alonzo <nospamvr-git@yahoo.com> - %{Version}-1
- Release de holaMundoRPM
