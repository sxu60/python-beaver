Name:           python-beaver
Version:        33.0.0
Release:        1%{?dist}
Summary:        Python beaver

Group:          Development/Languages
License:        MIT
URL:            https://github.com/josegonzalez/python-beaver
Source:         %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-setuptools
Requires: python-argparse
Requires: python-glob2
Requires: python-daemon
Requires: python-redis

%description
The Python beaver package.

%prep
%setup -q -n %{name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}


%files
%doc COPYING COPYING.LESSER README.rst
%{python_sitelib}/*
%exclude %{python_sitelib}/github/tests


%changelog
* Thu Dec 25 2014 Lucien Xu <sfietkonstantin@free.fr> - 33.0.0-1
- Initial package
