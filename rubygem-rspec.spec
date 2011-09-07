%define oname rspec

Name:           rubygem-%{oname}
Version:        2.6.0
Release:        %mkrel 1
Summary:        Behaviour Driven Development for Ruby
Group:          Development/Ruby
License:        MIT
URL:            http://rspec.info
Source0:        http://rubygems.org/downloads/%{oname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:       rubygems
Requires:       rubygem(rspec-core)
Requires:       rubygem(rspec-expectations)
Requires:       rubygem(rspec-mocks)
BuildRequires:  rubygems
BuildArch:      noarch
Provides:       rubygem(%{oname}) = %{version}

%description
Behaviour Driven Development for Ruby.

%prep

%build

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc --no-ri %{SOURCE0}

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%{ruby_gemdir}/gems/%{oname}-%{version}/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.markdown
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
