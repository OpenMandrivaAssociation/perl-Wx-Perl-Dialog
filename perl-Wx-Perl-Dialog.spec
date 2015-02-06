%define realname   Wx-Perl-Dialog

Name:		perl-%{realname}
Version:	0.04
Release:	4
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Abstract dialog class for simple dialog creation
Source:		http://www.cpan.org/modules/by-module/Wx/%{realname}-%{version}.tar.gz
Url:		http://search.cpan.org/dist/%{realname}

BuildRequires:	perl-devel
BuildRequires:	perl(File::Copy::Recursive)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Wx)
BuildRequires:	perl(Wx::Event)
BuildRequires:	perl(Wx::STC)

BuildArch:	noarch

%description
Abstract dialog class for simple dialog creation.

%prep
%setup -q -n %{realname}-%{version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
# requires GTK display
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Tue Dec 16 2008 Jérôme Quelin <jquelin@mandriva.org> 0.04-1mdv2009.1
+ Revision: 314761
- update to 0.04

* Mon Nov 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2009.1
+ Revision: 306194
- update to new version 0.03

* Tue Nov 11 2008 Jérôme Quelin <jquelin@mandriva.org> 0.02-1mdv2009.1
+ Revision: 302303
- added even more build prereq (this time they should be all here)
- added another missing prereq
- adding missing build prerequisite
- import perl-Wx-Perl-Dialog


* Tue Nov 11 2008 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist

