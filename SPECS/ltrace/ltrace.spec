Summary:	ltrace intercepts and records dynamic library calls.
Name:		ltrace
Version:	0.7.3
Release:	5%{?dist}
License:	GPLv2+
URL:		http://www.ltrace.org/
Group:		Development/Debuggers
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://www.ltrace.org/%{name}_%{version}.orig.tar.bz2
%define sha512 ltrace=a842b16dcb81da869afa0bddc755fdff0d57b35672505bf2c7164fd983b1938d28b126714128930994cc1230ced69d779456d0cfc16f4008c9b6d19f0852285d
Patch0:		Move-get_hfa_type-from-IA64-backend-to-type.c-name-i.patch
Patch1:		Set-child-stack-alignment-in-trace-clone.c.patch
Patch2:		Implement-aarch64-support.patch
Patch3:		add-missing-stdint.h-include.patch
Patch4:		Add-missing-include-stdio.h.patch
BuildRequires:	elfutils-libelf-devel
Requires:	elfutils-libelf
%description
ltrace intercepts and records dynamic library calls which are called by an executed process and the signals received by that process. It can also intercept and print the system calls executed by the program.

%prep
# Using autosetup is not feasible
%setup -q
%ifarch aarch64
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%endif

%build
autoreconf -fiv
%configure \
	--disable-werror

make %{?_smp_mflags}

%install
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%check
make %{?_smp_mflags} check

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_sysconfdir}/ltrace.conf
%{_bindir}/*
%{_datadir}
%changelog
* Fri Jan 06 2023 Vamsi Krishna Brahmajosyula <vbrahmajosyula@vmware.com> 0.7.3-5
- Bump up due to change in elfutils
* Tue Nov 14 2017 Alexey Makhalov <amakhalov@vmware.com> 0.7.3-4
- Aarch64 support
* Mon Oct 03 2016 ChangLee <changLee@vmware.com> 0.7.3-3
- Modified check
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 0.7.3-2
- GA - Bump release of all rpms
* Wed Nov 25 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.7.3-1
- Initial build.	First version
