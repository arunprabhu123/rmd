Name:           rmd
Version:        1.0
Release:        1%{?dist}
Summary:        Resource Management Daemon-RMD
License:        ASL 2.0
URL:            https://github.com/intel/rmd
Source0:        https://github.com/arunprabhu123/rmd/blob/master/rmd-1.0.tar.gz

BuildRequires:  go
BuildRequires:  make
BuildRequires:  pam-devel
# this package does not support big endian arch so far,
# and has been verified only on Intel platforms.
ExclusiveArch: %{ix86} x86_64


%description
Resource Management Daemon (RMD) is a system daemon running on Linux platforms

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_bindir}/
install -p -m 755 %{_builddir}/%{name}-%{version}/build/linux/x86_64/rmd %{buildroot}/%{_bindir}/
install -p -m 755 %{_builddir}/%{name}-%{version}/build/linux/x86_64/gen_conf %{buildroot}/%{_bindir}/

install -d %{buildroot}/%{_mandir}/man8
install -m 0644  %{_builddir}/%{name}-%{version}/rmd.8 %{buildroot}/%{_mandir}/man8
ln -sf %{_mandir}/man8/rmd.8 %{buildroot}/%{_mandir}/man8/gen_conf.8

mkdir -p %{buildroot}/%{_prefix}/local/etc/scripts
install -m 755  %{_builddir}/%{name}-%{version}/scripts/install.sh %{buildroot}/%{_prefix}/local/etc/scripts
install -m 755  %{_builddir}/%{name}-%{version}/scripts/setup_rmd_users.sh %{buildroot}/%{_prefix}/local/etc/scripts
install -m 755  %{_builddir}/%{name}-%{version}/scripts/build.sh %{buildroot}/%{_prefix}/local/etc/scripts
install -m 755  %{_builddir}/%{name}-%{version}/scripts/hacking.sh %{buildroot}/%{_prefix}/local/etc/scripts
install -m 755  %{_builddir}/%{name}-%{version}/scripts/test.sh %{buildroot}/%{_prefix}/local/etc/scripts
install -m 755  %{_builddir}/%{name}-%{version}/scripts/deps.sh %{buildroot}/%{_prefix}/local/etc/scripts
install -m 755  %{_builddir}/%{name}-%{version}/scripts/hacking_v2.sh %{buildroot}/%{_prefix}/local/etc/scripts
install -m 755  %{_builddir}/%{name}-%{version}/scripts/setup_pam_files.sh %{buildroot}/%{_prefix}/local/etc/scripts
install -m 755  %{_builddir}/%{name}-%{version}/scripts/build-opts-get %{buildroot}/%{_prefix}/local/etc/scripts/build-opts-get
install -m 755  %{_builddir}/%{name}-%{version}/scripts/go-env %{buildroot}/%{_prefix}/local/etc/scripts

mkdir -p %{buildroot}/%{_prefix}/local/etc/rmd
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/cpu_map.toml %{buildroot}/%{_prefix}/local/etc/rmd
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/policy.toml %{buildroot}/%{_prefix}/local/etc/rmd
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/policy.yaml %{buildroot}/%{_prefix}/local/etc/rmd
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/rmd.toml %{buildroot}/%{_prefix}/local/etc/rmd

mkdir -p %{buildroot}/%{_prefix}/local/etc/rmd/acl/roles/admin
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/acl/roles/admin/cert.pem %{buildroot}/%{_prefix}/local/etc/rmd/acl/roles/admin

mkdir -p %{buildroot}/%{_prefix}/local/etc/rmd/acl/roles/user
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/acl/roles/user/user-cert.pem %{buildroot}/%{_prefix}/local/etc/rmd/acl/roles/user

mkdir -p %{buildroot}/%{_prefix}/local/etc/rmd/acl/url
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/acl/url/model.conf %{buildroot}/%{_prefix}/local/etc/rmd/acl/url
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/acl/url/policy.csv %{buildroot}/%{_prefix}/local/etc/rmd/acl/url

mkdir -p %{buildroot}/%{_prefix}/local/etc/rmd/cert/client
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/cert/client/ca.pem %{buildroot}/%{_prefix}/local/etc/rmd/cert/client
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/cert/client/cert.pem %{buildroot}/%{_prefix}/local/etc/rmd/cert/client
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/cert/client/key.pem %{buildroot}/%{_prefix}/local/etc/rmd/cert/client
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/cert/client/user-cert.pem %{buildroot}/%{_prefix}/local/etc/rmd/cert/client
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/cert/client/user-key.pem %{buildroot}/%{_prefix}/local/etc/rmd/cert/client

mkdir -p %{buildroot}/%{_prefix}/local/etc/rmd/cert/server
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/cert/server/ca.pem %{buildroot}/%{_prefix}/local/etc/rmd/cert/server
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/cert/server/rmd-cert.pem %{buildroot}/%{_prefix}/local/etc/rmd/cert/server
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/cert/server/rmd-key.pem %{buildroot}/%{_prefix}/local/etc/rmd/cert/server

mkdir -p %{buildroot}/%{_prefix}/local/etc/rmd/pam
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/pam/rmd %{buildroot}/%{_prefix}/local/etc/rmd/pam

mkdir -p %{buildroot}/%{_prefix}/local/etc/rmd/pam/test
install -m 0644  %{_builddir}/%{name}-%{version}/etc/rmd/pam/test/rmd %{buildroot}/%{_prefix}/local/etc/rmd/pam/test

%files
%{_bindir}/%{name}
%{_bindir}/gen_conf
%{_mandir}/man8/rmd.8.gz
%{_mandir}/man8/gen_conf.8.gz
%{_prefix}/local/etc/scripts
%{_prefix}/local/etc/rmd
%doc README.md
%license LICENSE

%post
%{_prefix}/local/etc/scripts/install.sh --skip-pam-userdb

%changelog
* Tue Jan 07 2020 ArunPrabhu Vijayan <arunprabhu.vijayan@intel.com> - 1.0-1
- RMD package version 1.0
