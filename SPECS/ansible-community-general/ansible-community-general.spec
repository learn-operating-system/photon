%global collection_namespace community
%global collection_name general

Summary:        Modules and plugins supported by Ansible community
Name:           ansible-community-general
Version:        6.1.0
Release:        1%{?dist}
License:        GPL-3.0-or-later AND BSD-2-Clause AND MIT AND PSF-2.0
URL:            https://github.com/ansible-collections/community.general
Group:          Development/Libraries
Vendor:         VMware, Inc.
Distribution:   Photon

Source0: https://github.com/ansible-collections/community.general/archive/refs/tags/%{name}-%{version}.tar.gz
%define sha512 %{name}-%{version}=01a32428e97477527b8903b4293eccf9c50aa3e2e7302bc73fac32afb25c1b0400cb080b0a83e692c8be66b7d6661a3533f9d6de544c8f25edcc5356cd65e905

BuildArch: noarch

BuildRequires: ansible-devel

Requires: ansible

%description
This repository contains the community.general Ansible Collection. The collection is a part of the
Ansible package and includes many modules and plugins supported by Ansible community which are not
part of more specialized community collections.

%prep
%autosetup -p1 -n community.general-%{version}
rm -vr .github .azure-pipelines
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
find -type f -name '.gitignore' -print -delete

%build
export LANG="en_US.UTF-8" LC_ALL="en_US.UTF-8"
%{ansible_collection_build}

%install
export LANG="en_US.UTF-8" LC_ALL="en_US.UTF-8"
%{ansible_collection_install}
rm -vr %{buildroot}%{ansible_collection_files}/%{collection_name}/tests

%files
%defattr(-, root, root)
%{ansible_collection_files}

%changelog
* Tue Dec 13 2022 Gerrit Photon <photon-checkins@vmware.com> 6.1.0-1
- Automatic Version Bump
* Fri Nov 25 2022 Shreenidhi Shedi <sshedi@vmware.com> 6.0.1-1
- Upgrade to v6.0.1
* Tue Oct 25 2022 Gerrit Photon <photon-checkins@vmware.com> 5.8.0-1
- Automatic Version Bump
* Thu Oct 06 2022 Gerrit Photon <photon-checkins@vmware.com> 5.7.0-1
- Automatic Version Bump
* Wed Sep 28 2022 Nitesh Kumar <kunitesh@vmware.com> 5.6.0-1
- Initial version
