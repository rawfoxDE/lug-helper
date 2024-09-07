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
 
%clean
rm -rf %{buildroot}
