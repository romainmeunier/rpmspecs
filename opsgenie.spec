# Created by pyp2rpm-3.3.3
%global pypi_name opsgenie-sdk

Name:           python-%{pypi_name}
Version:        0.3.1
Release:        1%{?dist}
Summary:        Python SDK for OpsGenie Web/REST API

License:        Apache License 2.0
URL:            https://github.com/opsgenie/opsgenie-python-sdk
Source0:        https://files.pythonhosted.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(certifi) >= 14.05.14
BuildRequires:  python3dist(coverage) >= 4.0.3
BuildRequires:  python3dist(httpretty) >= 0.8.14
BuildRequires:  python3dist(nose2) >= 0.6.4
BuildRequires:  python3dist(pluggy) >= 0.3.1
BuildRequires:  python3dist(py) >= 1.4.31
BuildRequires:  python3dist(python-dateutil) >= 2.5.3
BuildRequires:  python3dist(pytz) >= 2016.1
BuildRequires:  python3dist(randomize) >= 0.13
BuildRequires:  python3dist(requests) >= 2.9.1
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools) >= 20.3.1
BuildRequires:  python3dist(six) >= 1.10.0
BuildRequires:  python3dist(tox)
BuildRequires:  python3dist(urllib3) >= 1.15.1

%description
OpsGenie Python SDK - [BETA] Aim and Scope -OpsGenie Python SDK aims to access
OpsGenie Web API through HTTP calls from a client application in Python
language.OpsGenie Python SDK covers:- Alert APIFuture releases are subject to
be delivered for packing more APIs soon.For more information about OpsGenie
Python SDK, please refer to OpsGenie Python API < document.Pre-requisites The
API is...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(certifi) >= 14.05.14
Requires:       python3dist(python-dateutil) >= 2.5.3
Requires:       python3dist(pytz) >= 2016.1
Requires:       python3dist(requests) >= 2.9.1
Requires:       python3dist(setuptools) >= 20.3.1
Requires:       python3dist(six) >= 1.10.0
Requires:       python3dist(urllib3) >= 1.15.1
%description -n python3-%{pypi_name}
OpsGenie Python SDK - [BETA] Aim and Scope -OpsGenie Python SDK aims to access
OpsGenie Web API through HTTP calls from a client application in Python
language.OpsGenie Python SDK covers:- Alert APIFuture releases are subject to
be delivered for packing more APIs soon.For more information about OpsGenie
Python SDK, please refer to OpsGenie Python API < document.Pre-requisites The
API is...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/opsgenie
%{python3_sitelib}/samples
%{python3_sitelib}/opsgenie_sdk-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Aug 13 2019 root - 0.3.1-1
- Initial package
