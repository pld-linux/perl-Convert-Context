%define         perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Perl Convert-Context module
Summary(pl):	Modu³ Perla Convert-Context
Name: 		perl-Convert-Context
Version: 	0.501
Release: 	4
Copyright:	GPL
Group: 		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source: 	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Convert/Convert-Context-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Convert-Context allows you to access attributed strings similiar to perl's 
normal strings.

%description -l pl
Convert-Context umo¿liwia dostêp do ³añcuchów z przyporz±dkowanymi atrybutami 
w podobny sposób jak do normalnych ³añcuchów.

%prep
%setup -q -n Convert-Context-%{version}

%build
perl Makefile.PL

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_archlib}

make install \
	DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Convert/Context/
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%{perl_sitelib}/Convert/Context.pm
%{perl_sitearch}/auto/Convert/Context

%{_mandir}/man3/*
