Summary:        tzinfo object for the local timezone.
Name:           python3-tzlocal
Version:        4.2
Release:        1%{?dist}
License:        MIT License
Group:          Development/Languages/Python
Vendor:         VMware, Inc.
Distribution:   Photon
Url:            https://pypi.python.org/pypi/tzlocal/1.4
Source0:        https://files.pythonhosted.org/packages/source/t/tzlocal/tzlocal-%{version}.tar.gz
%define sha512  tzlocal=5d1000bd8756ca2678655dbeedcfd6ef8d709503293303c98a48af234aca0d1525913585d679759c6fd7d4c5ef046c98384ee6e7a9eba769f81d05173ff0d77f
%if 0%{?with_check}
Patch0:         tzlocal-make-check-fix.patch
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-libs
BuildRequires:  python3-six
BuildRequires:  python3-setuptools
BuildRequires:  python3-xml
%if %{with_check}
BuildRequires:  curl-devel
%endif
Requires:       python3
Requires:       python3-libs
Requires:       python3-pytz
BuildArch:      noarch

%description
This Python module returns a tzinfo object with the local timezone information under Unix and Win-32.
It requires pytz, and returns pytz tzinfo objects. This module attempts to fix a glaring hole in pytz,
that there is no way to get the local timezone information, unless you know the zoneinfo name,
and under several Linux distros that’s hard or impossible to figure out.
Also, with Windows different timezone system using pytz isn’t of much use,
unless you separately configure the zoneinfo timezone name.
With tzlocal you only need to call get_localzone(),
and you will get a tzinfo object with the local time zone info.
On some Unices you will still not get to know what the timezone name is,
but you don’t need that when you have the tzinfo file.
However, if the timezone name is readily available it will be used.

%prep
%autosetup -p1 -n tzlocal-%{version}

%build
%py3_build

%install
%py3_install

%check
#One test is failing, have a git issue raised against it.
#https://github.com/regebro/tzlocal/issues/89
python3 setup.py test

%files
%defattr(-,root,root)
%{python3_sitelib}/*

%changelog
* Sun Aug 21 2022 Gerrit Photon <photon-checkins@vmware.com> 4.2-1
- Automatic Version Bump
* Fri Jul 24 2020 Gerrit Photon <photon-checkins@vmware.com> 2.1-1
- Automatic Version Bump
* Mon Jun 15 2020 Tapas Kundu <tkundu@vmware.com> 1.5.1-3
- Mass removal python2
* Mon Nov 26 2018 Tapas Kundu <tkundu@vmware.com> 1.5.1-2
- Fix make check
* Sun Sep 09 2018 Tapas Kundu <tkundu@vmware.com> 1.5.1-1
- Update to version 1.5.1
* Mon Sep 11 2017 Xiaolin Li <xiaolinl@vmware.com> 1.4-1
- Initial packaging for Photon
