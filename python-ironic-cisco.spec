%global plugin_vendor Cisco
%global srcname cisco_ironic_contrib
%global package_name cisco-ironic-contrib
%global docpath doc/build/html

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-ironic-cisco
Version:        XXX
Release:        XXX
Summary:        %{plugin_vendor} Ironic Integration

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{package_name}
Source0:        https://pypi.python.org/packages/source/c/%{package_name}/%{package_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python2-devel
BuildRequires:  python-mock
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx
BuildRequires:  python-testrepository
BuildRequires:  python-testtools

Requires:       python-babel
Requires:       python-pbr
Requires:       python-ImcSdk

%if 0%{?rhel} && 0%{?rhel} < 8
%{?systemd_requires}
%else
%{?systemd_ordering} # does not exist on EL7
%endif

%description
This package contains %{plugin_vendor} Ironic plugins for OpenStack.

%prep
%autosetup -n %{package_name}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
rm -f requirements.txt

# Kill egg-info in order to generate new SOURCES.txt
rm -rf %{srcname}.egg-info

%build
export SKIP_PIP_INSTALL=1
%{__python2} setup.py build
%{__python2} setup.py build_sphinx
rm %{docpath}/.buildinfo

%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%license LICENSE
%doc README.rst
%doc %{docpath}
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}-%{version}-py%{python2_version}.egg-info


%changelog
