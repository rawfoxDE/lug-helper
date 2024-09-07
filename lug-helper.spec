%global dist .fc40
Name: lug-helper
Version: 2.18
Release: 1%{?dist}
Summary: lug-helper prepares the system and installes StarCitizen on Linux

License: GPLv3+

%description
lug-helper prepares the system and installs the StarCitizen game on Linux
 
%prep
 
%build
%make_build
 
%install
%make_install
 
%files
%defattr(-,root,root,-)
%doc README.md
.libs/*
%dir %{_datadir}/cdplayer
 
%changelog
See on the project page at Github
https://github.com/starcitizen-lug/lug-helper
 
%clean
rm -rf %{buildroot}
