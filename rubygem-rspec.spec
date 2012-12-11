%define oname rspec

Name:           rubygem-%{oname}
Version:        2.8.0
Release:	2
Summary:        Behaviour Driven Development for Ruby
Group:          Development/Ruby
License:        MIT
URL:            http://rspec.info
Source0:        http://rubygems.org/downloads/%{oname}-%{version}.gem
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


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.8.0-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Tue Jan 24 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.8.0-1
+ Revision: 767859
- files listed twice fix
- version update 2.8.0

* Sat Sep 10 2011 Alexander Barakin <abarakin@mandriva.org> 2.6.0-2
+ Revision: 699183
- after bootstrap

* Wed Sep 07 2011 Alexander Barakin <abarakin@mandriva.org> 2.6.0-1
+ Revision: 698598
- imported package rubygem-rspec

* Wed Dec 01 2010 Rémy Clouard <shikamaru@mandriva.org> 2.0.1-1mdv2011.0
+ Revision: 604517
- Bump release
- fix url
- fix file list
- TODO: import subpackages

* Sun Oct 10 2010 Rémy Clouard <shikamaru@mandriva.org> 1.3.0-1mdv2011.0
+ Revision: 584522
- import rubygem-rspec

