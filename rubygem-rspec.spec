%define oname rspec

Name:           rubygem-%{oname}
Version:        3.1.0
Release:	2
Summary:        Behaviour Driven Development for Ruby
Group:          Development/Ruby
License:        MIT
URL:            https://rspec.info
Source0:        http://rubygems.org/downloads/rspec-3.1.0.gem
BuildRequires:  rubygems
Requires:       rubygem(rspec-core)
Requires:       rubygem(rspec-expectations)
Requires:       rubygem(rspec-mocks)
BuildRequires:  ruby
BuildArch:      noarch
Provides:       rubygem(%{oname}) = %{version}

%description
Behaviour Driven Development for Ruby.

%prep

%build

%install
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc --no-ri %{SOURCE0}

%files
%{ruby_gemdir}/gems/%{oname}-%{version}/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
