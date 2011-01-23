Summary:	MetAid - a tiny library for aiding metaprogramming
Summary(pl.UTF-8):	MetAid - mała biblioteka wspomagająca metaprogramowanie
Name:		ruby-metaid
Version:	1.0
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/8124/metaid-1.0.gem
# Source0-md5:	00e7415d280df58cd6922817de3192e9
URL:		http://rubyforge.org/projects/metaid/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb >= 3.3.1
Requires: ruby-builder
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MetAid is a tiny library for aiding metaprogramming.

%description -l pl.UTF-8
MetAid to mała biblioteka wspomagająca metaprogramowanie.

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
cp %{_datadir}/setup.rb .

%build
mkdir lib
mv metaid.rb lib

ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/metaid*
