%global dist .fc40
Name: lug-helper
Version: 2.18
Release: 1%{?dist}
Summary: lug-helper prepares the system and installes StarCitizen on Linux

License: GPLv3+

%description
lug-helper prepares the system and installs the StarCitizen game on Linux
 
%prep
%setup -q

%build
 
%install
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/usr/local/lib
install -m 755 %{name} %{buildroot}/usr/local/bin/%{lug-helper.sh}
install -m 755 %{name} %{buildroot}/usr/local/lib/%{lutris-starcitizen.json}
install -m 755 %{name} %{buildroot}/usr/local/lib/%{sc-launch.sh}

%files
/usr/local/bin/lug-helper.sh
/usr/local/bin/lutris-starcitizen.json
/usr/local/bin/sc-launch.sh

%changelog
* Sat Sep 07 2024 rawfox <rawfoxde@gmail.com> - 2.18-1
- First copr package
- Introducing Fedora COPR supported packages

%clean
rm -rf %{buildroot}
