%define oname rspec

Name:           rubygem-%{oname}
Version:        1.3.0
Release:        %mkrel 1
Summary:        Behaviour Driven Development for Ruby
Group:          Development/Ruby
License:        MIT
URL:            http://rspec.info
Source0:        http://gems.rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:       rubygems
Requires:       rubygem(cucumber) >= 0.3
Requires:       rubygem(fakefs) >= 0.2.1
Requires:       rubygem(syntax) >= 1.0
Requires:       rubygem(diff-lcs) >= 1.1.2
Requires:       rubygem(heckle) >= 1.4.3
Requires:       rubygem(hoe) >= 2.3.3
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
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%{_bindir}/autospec
%{_bindir}/spec
%{ruby_gemdir}/gems/%{oname}-%{version}/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/License.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Manifest.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/TODO.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/examples/failing/README.txt
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
