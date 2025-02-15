Summary:        Policy analysis tools for SELinux
Name:           setools
Version:        4.4.0
Release:        2%{?dist}
License:        GPLv2, LGPLv2.1
Group:          System Environment/Libraries
Url:            https://github.com/SELinuxProject/selinux/wiki
Vendor:         VMware, Inc.
Distribution:   Photon

Source0:        https://github.com/SELinuxProject/setools/releases/download/%{version}/%{name}-%{version}.tar.bz2
%define sha512  %{name}=2ec92d7a6e30261549b6a8d2f17175d4a7d8313ef0cd81f4a19a91c53fe0107bac9a89c19dd67a4c534ee51ec520590795b4312f9e03e69fdf1763b0c35291f8

BuildRequires:  cython3
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  libselinux-devel

Requires:       python3
Requires:       libselinux
Requires:       libsepol
# setools use networkx library, which we do not have.
# It can be installed by: pip3 install networkx
#Requires:       networkx

%description
Policy analysis tools for SELinux

%prep
%autosetup -p1 -n %{name}
sed -i "s/, 'networkx>=2.0'//" setup.py

%build
python3 setup.py build_ext
%py3_build

%install
%py3_install
# do not package ru man pages
rm -rf %{buildroot}%{_mandir}/ru

%files
%defattr(-,root,root,-)
%{_bindir}/sesearch
%{_bindir}/sechecker
%{_bindir}/apol
%{_bindir}/seinfoflow
%{_bindir}/sedta
%{_bindir}/seinfo
%{_bindir}/sediff
%{python3_sitelib}/*
%{_mandir}/man1/*

%changelog
* Fri Dec 02 2022 Prashant S Chauhan <psinghchauha@vmware.com> 4.4.0-2
- Update release to compile with python 3.11
* Mon Apr 12 2021 Gerrit Photon <photon-checkins@vmware.com> 4.4.0-1
- Automatic Version Bump
* Fri Nov 06 2020 Tapas Kundu <tkundu@vmware.com> 4.3.0-2
- Build with python 3.9
* Fri May 01 2020 Alexey Makhalov <amakhalov@vmware.com> 4.3.0-1
- Initial build.
