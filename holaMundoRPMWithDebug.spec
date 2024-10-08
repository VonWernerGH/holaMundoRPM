Name:           holaMundo
Version:       	1.0.0 
Release:        1%{?dist}
Summary:        Programa holaMundo, imprime "Hola Mundo"
License:        GPLv3
URL:           	https://github.com/VonWernerGH/
Source0:        %{name}-%{version}.tar.gz


%description
Programa que imprime "Hola Mundo"

%prep
%setup -q

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}

%files
%{_bindir}/%{name}

%changelog
* Mon Oct 07 2024 Víctor Emmanuel Rivero Alonzo <nospamvr-git@yahoo.com> - %{Version}-1
- Release de holaMundo
